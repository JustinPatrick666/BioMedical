// src/main.ts
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import * as cornerstone from 'cornerstone-core'
import * as cornerstoneWADOImageLoader from 'cornerstone-wado-image-loader'
import * as dicomParser from 'dicom-parser'
import { initCornerstone } from '@/composables/useDicom'

const startApp = async () => {
  // 初始化图像加载器
  cornerstoneWADOImageLoader.external.cornerstone = cornerstone
  cornerstoneWADOImageLoader.webWorkerManager.initialize({
    maxWebWorkers: navigator.hardwareConcurrency || 1,
    startWebWorkersOnDemand: true,
  })

  // 注册 WADO 图像加载器
  cornerstone.registerImageLoader('wadors', cornerstoneWADOImageLoader.wadors.ImageLoader)

  // 配置 dicomParser
  cornerstoneWADOImageLoader.external.dicomParser = dicomParser

  // 初始化 Cornerstone 和工具
  await initCornerstone()

  // 启动 Vue 应用
  const app = createApp(App)
  app.use(router)
  app.mount('#app')
}

startApp()
