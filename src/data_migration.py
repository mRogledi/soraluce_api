# import SavvyAPI_PeticionesData as spd
from datetime import date,datetime
import restClient
import pandas as pd
import json
import os
import calendar

machine_id = 'RGP_D5TDHU'


def create_indicator_registry():
    df = pd.DataFrame(columns=['indicator_id','indicator_name','group_id','extraction_date'])

    indicators_list = restClient.listIndicators(machine_id)
    for indicator in indicators_list:
        indicator_id = indicator['indicatorId']
        indicator_name = indicator['indicatorName']
        group_id = indicator['indicatorGroup']['groupId']
        df_i = {
            'indicator_id' : indicator_id,
            'indicator_name': indicator_name,
            'group_id':group_id,
            'extraction_date' : date.today(),
        }
        df = df.append(df_i, ignore_index=True)
    df.to_csv('./indicator_registry.csv')





def group_data_extraction(date_from,date_to,path_to_save_csv):
    data = restClient.getData('RGP_D5TDHU','0',date_from,date_to)
    print(f'API DATA REQUEST DONE - {datetime.now()}')
    group_list = data['data'][0]['data']
    print(f'Group qta: {len(group_list)}')
    # os.makedirs(os.getcwd()+'group_data/today')
    for group in group_list:
        group_id = group['group']
        group_data = group['data']
        df = pd.DataFrame(columns=['timestamp','indicatorId','value'])
        print(f'{group_id} : {len(group_data)} data')
        gd_list = []
        for gd in group_data:
            kpi_dict = dict(filter(lambda x: x[0] != 'timestamp', gd.items()))
            kpi_list = list(map(lambda x: {
                'indicatorId' : x[0],
                'value':x[1],
            }, kpi_dict.items()))

            gd_list.extend([{
                'timestamp':gd['timestamp'],
                'indicatorId': x['indicatorId'],
                'value': x['value']
            } for x in kpi_list])
            
        df = pd.DataFrame(gd_list)
        df.to_csv(f'{path_to_save_csv}/{group_id}.csv')
        print(f'group {group_id} csv file saved')


print(f'START - {datetime.now()}')
cal = calendar.Calendar()
year = 2020
month = 11
epoch = datetime.utcfromtimestamp(0)

for day in cal.itermonthdays(year,month):
    if day > 2:
        print(f'GROUP DATA EXTRACTION START FOR : {day}-{month}')
        sd = datetime(year,month,day,0,0,0)
        ed = datetime(year,month,day,23,59,59)
        sd_millis = (sd - epoch).total_seconds() * 1000.0
        ed_millis = (ed - epoch).total_seconds() * 1000.0
        os.makedirs(os.getcwd()+f'/group_data/{year}/{sd.strftime("%b")}/{day}-{month}-{year}',exist_ok=True)
        path_to_save_csv = f'group_data/{year}/{sd.strftime("%b")}/{day}-{month}-{year}'
        print(int(sd_millis))
        print(ed_millis)
        group_data_extraction(f'{int(sd_millis)}',f'{int(ed_millis)}',path_to_save_csv)
        print(f'GROUP DATA EXTRACTION END FOR : {day} - {month}')
print(f'END - {datetime.now()}')





