/* -*- Mode: rjsx -*- */

/*******************************************
 * Copyright (2018)
 *  Marcus Dillavou <line72@line72.net>
 *  http://line72.net
 *
 * Montclair:
 *  https://github.com/line72/montclair
 *  https://montclair.line72.net
 *
 * Licensed Under the GPLv3
 *******************************************/

import GTFSRTParser from './GTFSRTParser';

class Configuration {
    constructor() {
        this.center = [36.166273, -86.781062];
        this.tileserver = {
            url: 'https://nashville.gotransitapp.com/tiles/{z}/{x}/{y}.png',
            subdomains: ''
        };
        this.agencies = [
            {
                name: 'Routes',
                parser: new GTFSRTParser('montclair', '/nashville-gtfs.zip',
                                         'https://nashville.gotransitapp.com/api/no.php/TMGTFSRealTimeWebService/vehicle/vehiclepositions.pb',
                                         'https://nashville.gotransitapp.com/api/no.php/TMGTFSRealTimeWebService/gtfs-realtime/trapezerealtimefeed.pb')
            }
        ];
    }
}

export default Configuration;
