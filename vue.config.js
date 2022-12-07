const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  outputDir: 'dist',
  assetsDir: 'static',
  publicPath:process.env.NODE_ENV === 'production'? '.': './'
})
