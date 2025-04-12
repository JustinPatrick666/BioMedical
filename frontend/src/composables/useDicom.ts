// src/composables/useDicom.ts
import * as cornerstone from 'cornerstone-core'
import * as cornerstoneTools from 'cornerstone-tools'
import Hammer from 'hammerjs'

export async function initCornerstone() {
  try {
    // 新版初始化方式（必须步骤）
    cornerstoneTools.external.cornerstone = cornerstone
    cornerstoneTools.external.Hammer = Hammer

    // 初始化工具库
    await cornerstoneTools.init({
      globalToolSyncEnabled: true,
      showSVGCursors: true
    })

    // 添加基础工具
    cornerstoneTools.addTool(cornerstoneTools.WwwcTool)
    cornerstoneTools.addTool(cornerstoneTools.PanTool)

    console.log('✅ Cornerstone初始化成功')
    return true
  } catch (error) {
    console.error('❌ Cornerstone初始化失败:', error)
    throw error
  }
}
