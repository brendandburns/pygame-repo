// webpack.config.js
module.exports = {
  mode: 'development',
  module: {
      rules: [
        {
          test: /\.py$/i,
          use: 'raw-loader',
        },
      ],
    },
  };