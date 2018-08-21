import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

function pos_to_freq(startFreq, endFreq, pos) {
        return startFreq**(1-pos) * endFreq ** pos;
}

new Vue({
  render: h => h(App)
}).$mount('#app')
