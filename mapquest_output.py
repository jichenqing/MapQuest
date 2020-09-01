#Sue Ji  33337876

import mapquest_APIs


class TotalDistance:
   
    def result(self,output:dict)->None:
        '''
        get the distance of one trip from mapquest dict and print it to client
        '''
        print('\nTOTAL DISTANCE:',round(output['route']['distance']),'miles')



class TotalTime:
    
    def result(self,output:dict)->None:
        '''
        get the estimated total time of one trip ftom mapquest dict and print it
        to the client
        '''
        info=output['route']['time']/60
        print('\nTOTAL TIME:',round(info),'minutes')



class Steps:
    
    def result(self,output:dict)->None:
        '''
        get the detailed directions from one place to another ftom mapquest
        dict and print it to the client
        '''
        print('\nDIRECTIONS')
        for leg in output['route']['legs']:
            for maneuver in leg['maneuvers']:
                print(maneuver['narrative'])
      


class Latlong:
    '''
    takes the output and returns the formatted latitude and longtitude
    with directions following each of them.
    '''
    def result(self,output:dict)->None:
        '''
        get the latitude+one of the SNEW + longtitude+
        one o the SNEW of one place ftom mapquest
        dict and print it to the client
        '''
        print('\nLATLONGS')
        
        for i in output['route']['locations']:
            lat=i['latLng']['lat']
            long=i['latLng']['lng']
            if lat>0:
                direction_lat='N'
            else:
                direction_lat='S'
                lat=-lat
            if long>0:
                direction_long='E'
            else:
                direction_long='W'
                long=-long
                
            print('{0:.2f}'.format(lat)+direction_lat+' {0:.2f}'.format(long)+\
                  direction_long)

    
    def _lat_longs(self,output:dict)->list:
        '''
        get the latitude and longitude of one place from mapquest
        dict and print it to the client
        '''
        info=output['route']['locations']
        result=[]
        for i in info:
            result.append(i['latLng']['lat'])
            result.append(i['latLng']['lng'])

        return result
                        

    

class Elevations:
    
    def result(self,output:dict)->None:
        '''
        get the elevation of one place from mapquest
        dict and print it to the client
        '''
        print('\nELEVATIONS')
        latlongs=Latlong()._lat_longs(output)
        for i in range(0,len(latlongs),2):
            latlong=str(latlongs[i])+','+str(latlongs[i+1])
            info=mapquest_APIs.get_result(mapquest_APIs.build_LatLong_url(latlong))
            for x in info['elevationProfile']:
                meters=int(x['height'])
                print(int(meters*3.28084))


