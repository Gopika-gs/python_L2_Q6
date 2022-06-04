color_dict = {'red':'#FF0000',
'green':'#008000',
'black':'#000000',
'white':'#FFFFFF'}
sorted_keys = sorted(color_dict.keys())
sorted_dict = {keys:color_dict[keys] for keys in sorted_keys}
print(sorted_dict)