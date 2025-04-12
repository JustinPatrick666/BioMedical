<template>
  <div class="dicom-container">
    <div ref="viewerElement" class="viewer-element"></div>
    <div class="toolbar">
      <el-slider
        v-model="windowWidth"
        :min="0"
        :max="2000"
        @input="updateViewport"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import cornerstone from 'cornerstone-core'
import * as dicomParser from 'dicom-parser'

const viewerElement = ref<HTMLElement>()
const windowWidth = ref(400)

const updateViewport = () => {
  if (!viewerElement.value) return
  const viewport = cornerstone.getViewport(viewerElement.value)
  viewport.voi.windowWidth = windowWidth.value
  cornerstone.setViewport(viewerElement.value, viewport)
}

onMounted(async () => {
  if (!viewerElement.value) return

  // 启用元素
  cornerstone.enable(viewerElement.value)
  console.log('启用元素:', viewerElement.value)

  try {
    // 加载图像
    const image = await cornerstone.loadImage('wadouri:http://localhost:3000/dicom/sample.dcm')
    console.log('图像加载完成:', image)

    // 显示图像
    cornerstone.displayImage(viewerElement.value, image)
    updateViewport()
  } catch (error) {
    console.error('图像加载失败:', error)
    if (viewerElement.value) {
      viewerElement.value.innerHTML = `
        <div style="color:red;padding:20px;text-align:center;">
          <p>图像加载失败: ${error.message}</p>
          <button onclick="location.reload()" style="padding:10px;background:#007bff;color:white;border:none;border-radius:5px;cursor:pointer;">
            重试
          </button>
        </div>
      `
    }
  }
})

onUnmounted(() => {
  if (viewerElement.value) {
    cornerstone.disable(viewerElement.value)
  }
})
</script>

<style scoped>
.dicom-container {
  width: 100%;
  height: 600px;
  position: relative;
}
.viewer-element {
  width: 100%;
  height: 100%;
  background-color: #000; /* 黑色背景便于观察 */
}
.toolbar {
  position: absolute;
  bottom: 10px;
  left: 0;
  right: 0;
  padding: 10px;
  background: rgba(0, 0, 0, 0.5);
}
</style>
