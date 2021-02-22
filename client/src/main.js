import Vue from 'vue'
import vuetify from './plugins/vuetify';
import firebase from 'firebase/app';

import App from './App.vue'
import firebaseConfig from './firebase';

Vue.config.productionTip = process.env.VUE_APP_API_NODE_ENV === 'PROD';
firebase.initializeApp(firebaseConfig);

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
