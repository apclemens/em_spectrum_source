<template>
    <div>
    </div>
</template>

<script>
import Classes from './../assets/info/classes.json'
import US from './../assets/info/us.json'
import NATO from './../assets/info/nato.json'
import IEEE from './../assets/info/ieee.json'
import TV from './../assets/info/tv_radio.json'
import Optical from './../assets/info/optical.json'
import UV from './../assets/info/uv.json'

// https://www.ntia.doc.gov/files/ntia/publications/2003-allochrt.pdf

export default {
    name: 'BandInfo',
    data() {
        var info = [[], [], [], []];
        var jsons = [
            Classes,
            US,
            NATO,
            IEEE,
            TV,
            Optical,
            UV,
        ];
        var band;
        for (var i=0; i<jsons.length; i++) {
            var json = jsons[i];
            for (var j=0; j<json.data.length; j++) {
                band = json.data[j];
                info[band.bar].push(band);
            }
        }
        return {
            information: info,
        }
    }
}
</script>

<style>
</style>
