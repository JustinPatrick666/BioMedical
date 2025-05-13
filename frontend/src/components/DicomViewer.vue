<template>
  <div class="dicom-viewer">
    <div id="dicomImageContainer" ref="dicomImageContainer"></div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import * as cornerstone from 'cornerstone-core';
import * as cornerstoneTools from 'cornerstone-tools';
import * as cornerstoneWADOImageLoader from 'cornerstone-wado-image-loader';

const dicomImageContainer = ref(null);

onMounted(() => {
  // 初始化 Cornerstone 和相关工具
  cornerstoneWADOImageLoader.external.cornerstone = cornerstone;
  cornerstoneTools.init();

  const element = dicomImageContainer.value;
  if (element) {
    cornerstone.enable(element);

    // 添加基本工具（如平移和缩放）
    cornerstoneTools.addTool(cornerstoneTools.PanTool);
    cornerstoneTools.addTool(cornerstoneTools.ZoomTool);
    cornerstoneTools.setToolActive('Pan', { mouseButtonMask: 1 }); // 左键平移
    cornerstoneTools.setToolActive('Zoom', { mouseButtonMask: 2 }); // 右键缩放

    // 加载 DICOM 图像
    loadDicomImage('/dicom/image-00000.dcm'); // 新的文件路径
  }
});

async function loadDicomImage(url: string) {
  const element = dicomImageContainer.value;

  if (!element) {
    console.error('DICOM 容器未找到');
    return;
  }

  try {
    // 加载 DICOM 图像
    const image = await cornerstone.loadImage(url);
    cornerstone.displayImage(element, image);
  } catch (error) {
    console.error('加载 DICOM 图像失败:', error);
  }
}
</script>

<style scoped>
.dicom-viewer {
  width: 100%;
  height: 100%;
  position: relative;
}

#dicomImageContainer {
  width: 100%;
  height: 100%;
  background-color: black; /* DICOM 查看器背景为黑色 */
}
</style>
