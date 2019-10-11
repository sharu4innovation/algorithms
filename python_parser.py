import pandas
import re
from pandas import DataFrame
import argparse


def get_matched_lists(each_line):
    user_name = re.search(r'Failed password for.(.*?) from', each_line)
    ip_address = re.search(r'from .(.*?) port', each_line)
    reverse_mapping = re.search(r'reverse mapping checking getaddrinfo for undefined.datagroup.ua .(.*?)] failed', each_line)
    return user_name, ip_address, reverse_mapping

def parse_file(filelines, **kwargs):
    input_date_formatted = kwargs.get("input_date_formatted")
    failed_attempt_row_list = []
    reverse_map_row_list = []
    fa_result = []
    rmap_result = []
    user_name, ip_address,reverse_mapping  = None, None, None
    for each_line in filelines:
        if input_date_formatted:
            if input_date_formatted in each_line:
                user_name, ip_address, reverse_mapping  = get_matched_lists(each_line)
        else:
            user_name, ip_address, reverse_mapping  = get_matched_lists(each_line)
        if user_name and ip_address:
            _dict = (user_name.group(1),ip_address.group(1))
            failed_attempt_row_list.append(_dict)
        elif reverse_mapping:
            reverse_map_row_list.append(reverse_mapping.group(1))
        else:
            pass
    if len(failed_attempt_row_list) > 0:
        df  = DataFrame(failed_attempt_row_list, columns = ['user_name', 'ip_address'])
        df = df.groupby(['user_name', 'ip_address']).agg({'ip_address':len}).rename(columns = {'ip_address': 'total_ip'}).reset_index()
        df = df.groupby(['user_name', 'ip_address']).agg({'ip_address':len}).rename(columns = {'ip_address': 'total_ip'}).reset_index()
        df = pandas.merge(df, df.groupby(['user_name']).agg({'total_ip':sum}).rename(columns={'total_ip':'total'}).reset_index(), on = ['user_name'])
        result_dict = {}
        def get_dict(x):
            result_dict.update({x['user_name'][0]:{'TOTAL':x['total'][0],'IPLIST' : dict(zip(x['ip_address'], x['total_ip']))}})
        df.groupby('user_name').apply(get_dict)
        if input_date_formatted:
            fa_result = {input_date_formatted: result_dict}
        else:
            fa_result = result_dict
            
    if len(reverse_map_row_list) > 0:
        result_dict = {'undefined.datagroup.ua': {'TOTAL':len(reverse_map_row_list),'IPList':list(set(reverse_map_row_list)) }}
        if input_date_formatted:
            rmap_result = {input_date: result_dict}
        else:
            rmap_result = result_dict
            
    return fa_result, rmap_result

def arg_parse():
    parser = argparse.ArgumentParser(description='Python Parser')
    parser.add_argument('--file',
                       metavar='file',
                       type=str,
                       help='path to file')
    parser.add_argument('--date',
                   metavar='date',
                   type=str,
                   help='date')

    args = parser.parse_args()
    return args.file, args.date

if __name__ == '__main__':
    file_path, input_date = arg_parse()
    
    with open('auth.log') as f:
        filelines = f.readlines()

    if input_date:
        input_date_formatted = pandas.to_datetime(input_date).strftime('%b %d')
        fa_result, rmap_result = parse_file(filelines, input_date_formatted = input_date_formatted)
    else:
        fa_result, rmap_result = parse_file(filelines)
    print(fa_result, rmap_result)        
