import Vue from 'vue'
import vuescroll from 'vue-scroll'
import App from './App.vue'

Vue.use(vuescroll)

Vue.config.productionTip = false

new Vue({
  render: h => h(App)
}).$mount('#app')
