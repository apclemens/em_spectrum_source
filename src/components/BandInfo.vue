<template>
    <div>
    </div>
</template>

<script>
import UHF_US from './../assets/info/uhf-us.json'
import Classes from './../assets/info/classes.json'
import US from './../assets/info/us.json'

// https://www.ntia.doc.gov/files/ntia/publications/2003-allochrt.pdf

export default {
    name: 'BandInfo',
    data() {
        var info = [[], [], [], []];
        var jsons = [
            Classes,
            US,
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
