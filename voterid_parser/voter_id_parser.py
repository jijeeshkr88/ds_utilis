import re


id_pattern = r'\s[A-Z]{3}[0-9]{7}'
age_pattern = r'Age :'
name_pattern = r'Name :'
parent_list = ["Mother's Name :","Husband's Name :","Father's Name :","Husband's   ",
"Mother's   ","Father's   "]
house_pattern = r'House No :'
gender_list = ["Age :","Gender :"]
number_pattern = r'\s[0-9]{1,3}\s'



def read_text(file_name):
	text_list = []
	file = open(file_name,'r')
	for line in file:
		text_list.append(line)
	return text_list


def content_detect(text_line):
	flag_list = []
	father_flag = False
	id_flag = False
	age_flag = False
	house_flag = False
	name_flag =  False
	content = []
	if "Age :" in text_line and ("Sex :" in text_line or "Gender :" in text_line):
		new_flag = 1
	else:
		new_flag = 0
	if len(re.findall(id_pattern,text_line))>1:
		start_flag = 1
	else:
		start_flag = 0
	if len(re.findall(id_pattern,text_line))>1:
		id_flag = True
		content = first_line(text_line)
	if len(re.findall(age_pattern,text_line))>1:
		age_flag = 	True
		content = age_parse(text_line)
	if len(re.findall(house_pattern,text_line))>1:
		house_flag = True
		content = house_parse(text_line)
	if len(re.findall(name_pattern,text_line))>1:
		name_flag = True
		content = name_parse(text_line)
	for i in parent_list:
		if i in text_line:
			father_flag = True
			content = gurdian_parse(text_line)
	return start_flag,new_flag,[father_flag ,id_flag ,age_flag ,house_flag ,name_flag],content


def first_line(line1):
	pan_list = re.findall(id_pattern,line1)
	count_list = re.findall(number_pattern,line1)
	return [{"id_":count_list},{"voter_ids":pan_list}]

def age_parse(line):
	age_list = []
	gender_ = []
	for seg in re.split(age_pattern,line):
		if len(seg)>2:
			for i in gender_list:
				sp_ =seg.split(i)
				if len(sp_)>1:
					print(sp_[0],sp_[1])
					age_list.append(sp_[0])
					gender_.append(sp_[1])
	return [{"age":age_list},{"gender":gender_}]

def house_parse(line):
	house_list = []
	for i in re.split(house_pattern,line):
		if len(i)>2:
			house_list.append(i)
	return [{"house":house_list}]

def name_parse(line):
	name_list = []
	for i in re.split(name_pattern,line):
		if len(i)>2:
			name_list.append(i)
	return [{"name":name_list}]

def gurdian_parse(line):
	gurdian_list = []
	for seg in line.split("     "):
		if len(seg)>1:
			for i in parent_list:
				sp = seg.split(i)
				if len(sp)>1:
					d = {i:sp[1]}
					gurdian_list.append(d)
	return [{"gurdian":gurdian_list}]

def segment_parse(text_):
	content_seg = []
	segment_list = []
	seg_parse = []
	parse_seg_list = []
	for i in text_:
		start_flag,endflag,flag_list,content = content_detect(str(i))
		if any(flag_list) and start_flag==1:
			content_seg = []
			seg_parse = []
			content_seg.append(i)
			seg_parse.append(content)
		if any(flag_list) and (start_flag==0 and endflag==0):
			content_seg.append(i)
			seg_parse.append(content)
		if any(flag_list) and endflag==1:
			content_seg.append(i)
			seg_parse.append(content)
			segment_list.append(content_seg)
			parse_seg_list.append(seg_parse)
	return segment_list,parse_seg_list


def parse_segment(segment_list):
	new_segments = []
	for seg in segment_list:
		seg_dict = voter_mat(seg)
		new_segments.append(seg_dict)	
	return new_segments


if __name__ == '__main__':
	file_name = "./data/sample_pdf.txt"
	text_ = read_text(file_name)
	segs,parsed_list = segment_parse(text_)










