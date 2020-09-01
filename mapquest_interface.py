#Sue Ji 33337876

import mapquest_APIs
import mapquest_output
import json
 
def _user_request()->list:
    '''
    takes the user input for all the addresses and returns them as a list
    '''
    user_input=int(input())
    if user_input>=2:
        locations=[]
        for address in range(user_input):
            locations.append(input())
        return locations
    else:
        exit()


def _request_info()->list:
    '''
    takes the user input and returns the requested info as a list
    '''
    info=[]
    info_num=int(input())
    if info_num>5 or info_num<1:
        exit()
    else:
        for asked_data in range(info_num):
            info.append(input())
        return info


def _run_class(output:dict,classes:['class'])->dict:
    '''
    takes the output, returns the info when the output matches the classes
    '''
    info=output
    for i in classes:
        i.result(info)
    return info



def _commands(userinput:list)->list:
    '''
    takes the user input and returns the requested classes info as a list
    '''
    infolist=[]
    for info in userinput:
        if info=='LATLONG':
            infolist.append(mapquest_output.Latlong())
        if info=='STEPS':
            infolist.append(mapquest_output.Steps())
        if info=='TOTALTIME':
            infolist.append(mapquest_output.TotalTime())
        if info=='TOTALDISTANCE':
            infolist.append(mapquest_output.TotalDistance())
        if info=='ELEVATION':
            infolist.append(mapquest_output.Elevations())
    return infolist



def _execute()->None:
    '''
    run the entire program under the if __name__=='__main__'
    '''
    try:
        locations=_user_request()
        classes=_request_info()
        route_info=mapquest_APIs.get_result(
    mapquest_APIs.build_locations_url(locations))
        for key in route_info['route']:
            if key=='routeError':
                print('\nNO ROUTE FOUND')
            else:
                _run_class(mapquest_APIs.get_result(
        mapquest_APIs.build_locations_url(locations)),_commands(classes))
                print("\nDirections Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors")
                break
            
    except:
        print('\nMAPQUEST ERROR')
        

if __name__=="__main__":
    '''
    RUNS THE WHOLE PROGRAM WHEN THE MODULE IS EXECUTED THE FIRST TIME
    '''
    _execute()
    
