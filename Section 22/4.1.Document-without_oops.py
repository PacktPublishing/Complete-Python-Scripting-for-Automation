#!/bin/python3
import os

def get_all_tomcats():
    list_of_config_files=[]
    for r,d,f in os.walk("/"):
        for each_file in f:
            if each_file=='server.xml':
                list_of_config_files.append(os.path.join(r,each_file))
    return list_of_config_files
def display_details(home_cnf_files):
    for each_key in home_cnf_files.keys():
        print(f'The Tomcat home is: {home_cnf_files[each_key][0]}')
        print(f'The Tomcat config file is:{home_cnf_files[each_key][1]}' )
    return None

def main():
    print("Finding list of tomcats...")
    list_of_tomcats=get_all_tomcats()
    #print(list_of_tomcats)
    cnt=1
    home_cnf_files={}
    for each_config_file in list_of_tomcats:
        t_home=os.path.dirname(os.path.dirname(each_config_file))
        t_cnf_file=each_config_file
        home_cnf_files['tomcat'+str(cnt)]=[t_home,t_cnf_file]
        cnt+=1
    #print(home_cnf_files)
    display_details(home_cnf_files)
    return None


if __name__ == '__main__':
    main()
