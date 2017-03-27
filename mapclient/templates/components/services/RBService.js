import util from './util';
import URL from 'url-parse';

const url = 'http://api.boundlessgeo.io/v1/basemaps/';
//const url = 'http://localhost:8000/'

class RBService {
  getTileServices(apiKey, callback) {
    util.doGET(url, function(xmlhttp) {
      var config = JSON.parse(xmlhttp.responseText);
      var results = [];
      for (var i = 0, ii = config.length; i < ii; i++) {
        var tileConfig = config[i];
        if (tileConfig.tileFormat == 'PNG' && tileConfig.standard == 'XYZ') {
          var urlObj = new URL(tileConfig.endpoint, true);
          urlObj.set('query', Object.assign(urlObj.query, {
            apikey: apiKey
          }));
          tileConfig.endpoint = urlObj.toString();
          if (!tileConfig.thumbnail) {
            tileConfig.thumbnail = tileConfig.endpoint.replace('{x}', '0').replace('{y}', '0').replace('{z}', '0').replace('{-y}', '0');
          }
          tileConfig.description = tileConfig.name;
          results.push(tileConfig);
        }
      }
      var addTileConfig;
      //addTileConfig.tileFormat = 'PNG';
      //addTileConfig.standard = 'XYZ';
      //addTileConfig.name = 'prova';
      //addTileConfig.endpoint = 'http://localhost:8000/maps/tms/map/2ea065644d3e505e7780172808fbd7cb/{z}/{x}/{y}?token=3257eb89f1ccfa18669350a1b1e9fbf9';
      //results.push(addTileConfig);
      callback.call(this, results);
    }, function() {
      callback.call(this, []);
    });
  }
}

export default new RBService();
