/* eslint-env node */
module.exports = {
  root: true,
  env: {
    node: true,
  },
  'extends': [
    // 'plugin:vue/vue3-essential',
    'eslint:recommended',
    'plugin:vue/vue3-recommended',
  ],
  parserOptions: {
    ecmaVersion: 'latest'
  },
  rules: {
    //...
    "vue/require-default-prop": "off",
  }
  
}
