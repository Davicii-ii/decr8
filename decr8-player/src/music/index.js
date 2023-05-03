const req = require.context('.', true, /\.js$/)
const modules = []

req.keys().forEach((filename) => {
  if (filename === './index.js') return
  const module = req(filename)
  modules.push(module.default || module)
})

export default modules
