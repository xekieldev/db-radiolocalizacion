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
    "vue/no-mutating-props": ["error", {
      "shallowOnly": true
    }],
    "vue/multi-word-component-names": ["error", {
      "ignores": ["Menu", "Heading"]
    }]
  }
  
}
