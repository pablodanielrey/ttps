import Vue from 'vue'
import ar from 'vee-validate/dist/locale/es';
import {
    ValidationProvider,
    Validator ,
    ValidationObserver
} from 'vee-validate';
// Inside a component.




// Also available on the prototype.
Validator.localize('ar',ar);



Vue.component('ValidationProvider', ValidationProvider);
Vue.component('ValidationObserver', ValidationObserver);