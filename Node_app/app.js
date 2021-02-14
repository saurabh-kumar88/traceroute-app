const Traceroute = require('nodejs-traceroute');
var geoip = require('geoip-lite');

class TraceRoute_App{

    runCommand(cmd){
         try {
            const tracer = new Traceroute();
            tracer
                .on('pid', (pid) => {
                    console.log(`pid: ${pid}`);
                })
                .on('destination', (destination) => {
                    console.log(`destination: ${destination}`);
                })
                .on('hop', (hop) => {
                    this.getLocation(hop.ip);
                    // console.log(`hop: ${JSON.stringify(hop)}`);
                })
                .on('close', (code) => {
                    console.log(`close: code ${code}`);
                });
         
            tracer.trace(cmd);
        } catch (ex) {
            console.log(ex);
        }
        
    }
    getLocation(ip){
        var geo = geoip.lookup(ip);
        if(! geo ) return ;
        console.log(`Country : ${ geo.country }, City : ${ geo.city }, Coordinates ${ geo.range }`);
    }


}

const obj = new TraceRoute_App()
obj.runCommand("google.com");

