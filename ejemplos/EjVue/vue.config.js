/* module.exports = {
    devServer: {
      proxy: {
        "/api": {
          target: "http://localhost:8000",
          changeOrigin: true,
          logLevel: "debug",
          pathRewrite: { "^/api": "/" }
        }
      }
    }
    
  }; */
  module.exports = {
  chainWebpack: config => {
    config.performance
      .maxEntrypointSize(400000)
      .maxAssetSize(400000)
  }
}