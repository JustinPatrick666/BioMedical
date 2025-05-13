<template>
  <div class="sidebar">
    <button id="load-dicom" @click="loadDicom">
      <i class="fas fa-upload"></i> 加载 DICOM
    </button>
    <button id="pan-tool" @click="setToolActive('Pan')" :class="{ active: activeTool === 'Pan' }">
      <i class="fas fa-arrows-alt"></i> 平移工具
    </button>
    <button id="zoom-tool" @click="setToolActive('Zoom')" :class="{ active: activeTool === 'Zoom' }">
      <i class="fas fa-search-plus"></i> 缩放工具
    </button>
    <button id="reset-view" @click="resetView">
      <i class="fas fa-sync-alt"></i> 重置视图
    </button>
    <button id="toggle-info" @click="toggleInfoPanel">
      <i class="fas fa-info-circle"></i> 显示/隐藏信息
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeTool: null, // 当前激活的工具
    };
  },
  methods: {
    loadDicom() {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = '.dcm';
      input.onchange = (event) => {
        const file = event.target.files[0];
        if (file) {
          console.log('加载 DICOM 文件:', file.name);
          // 在这里处理 DICOM 文件
        }
      };
      input.click();
    },
    setToolActive(toolName) {
      this.activeTool = toolName;
      console.log(`激活工具: ${toolName}`);
      // 调用 cornerstoneTools 设置工具
    },
    resetView() {
      console.log('重置视图');
      // 在这里实现重置视图逻辑
    },
    toggleInfoPanel() {
      console.log('切换信息面板');
      // 在这里实现显示/隐藏信息面板逻辑
    },
  },
};
</script>

<style scoped>
/* 局部样式 */
.sidebar button i {
  margin-right: 0.5rem;
}
</style>
