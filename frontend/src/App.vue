<template>
  <div id="app">
    <!-- 顶部导航栏 -->
    <header class="navbar">
      <h1>肿瘤影像自动分析系统</h1>
      <nav>
        <router-link to="/">首页</router-link>
        <router-link to="/about">关于</router-link>
      </nav>
    </header>

    <!-- 主体内容 -->
    <main class="container">
      <!-- 左侧工具栏 -->
      <aside class="sidebar">
        <h4>图像操作</h4>
        <button @click="loadImage">
          <i class="fas fa-upload"></i> 加载 DICOM 图像
        </button>
        <button @click="toggleMeasurement">
          <i class="fas fa-ruler"></i> 测量工具
        </button>
        <button @click="resetView">
          <i class="fas fa-sync-alt"></i> 重置视图
        </button>
        <button @click="adjustContrast">
          <i class="fas fa-adjust"></i> 调整对比度
        </button>
        <div>
         <label for="contrast">对比度:</label>
         <input type="range" id="contrast" min="0" max="2" step="0.1" value="1" @input="adjustContrast">
        </div>
      </aside>

      <Sidebar />
        <div class="main-content">主内容区</div>
        <div class="info-panel">信息面板</div>

      <!-- 中间主内容区 -->
      <section class="main-content">
        <DicomViewer />
      </section>

      <!-- 右侧信息面板 -->
      <aside class="info-panel">
        <h3>患者信息</h3>
        <p><strong>姓名:</strong> 张三</p>
        <p><strong>年龄:</strong> 45岁</p>
        <p><strong>性别:</strong> 男</p>
        <h3>AI 分析结果</h3>
        <p><strong>肿瘤类型:</strong> 恶性</p>
        <p><strong>肿瘤大小:</strong> 3.5cm x 2.8cm</p>
        <p><strong>风险评估:</strong> 高</p>
      </aside>
    </main>
  </div>
</template>

<script setup lang="ts">
import DicomViewer from '@/components/DicomViewer.vue';

function loadImage() {
  const input = document.createElement('input');
  input.type = 'file';
  input.accept = '.dcm'; // 只接受 DICOM 文件
  input.onchange = (event) => {
    const file = event.target.files[0];
    if (file) {
      console.log('加载 DICOM 文件:', file.name);
      // 将文件传递给 DicomViewer 组件
      // 示例：通过事件总线或状态管理工具（如 Pinia 或 Vuex）
      alert(`已加载文件: ${file.name}`);
    }
  };
  input.click();
}

function toggleMeasurement() {
  console.log('切换测量工具');
  // 示例：调用 Cornerstone.js 的工具 API
  // cornerstoneTools.setToolActive('Length', { mouseButtonMask: 1 });
  alert('测量工具已激活');
}

function resetView() {
  console.log('重置视图');
  // 示例：调用 Cornerstone.js 的 reset 视图方法
  // cornerstone.reset(element);
  alert('视图已重置');
}



function adjustContrast(event) {
  const contrast = parseFloat(event.target.value);
  console.log('调整对比度:', contrast);
  // 示例：调用 Cornerstone.js 的 setViewport 方法
  // cornerstone.setViewport(element, { ...viewport, invert: false, pixelReplication: false });
  alert(`对比度已调整为: ${contrast}`);
}

</script>

<style scoped>
.navbar {
  display: flex;
  font-family: 'Roboto', sans-serif;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: var(--vt-c-primary);
  color: #0f66ab;
}

.navbar nav a {
  font-family: 'Roboto', sans-serif;
  margin: 0 1rem;
  text-decoration: none;
  color: #0f66ab;
  font-weight: bold;
}

.navbar nav a.router-link-active {
  font-family: 'Roboto', sans-serif;
  text-decoration: underline;
}

.container {
  display: grid;
  grid-template-columns: 200px 1fr 300px;
  gap: 1rem;
  padding: 1rem;
  height: calc(100vh - 60px);
}

.sidebar, .main-content, .info-panel {
  background-color: rgba(255, 255, 255, 0.05); /* 半透明背景 */
  border-radius: 8px;
  padding: 1rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}

.sidebar button {
  font-family: 'Roboto', sans-serif;
  width: 100%;
  margin-bottom: 0.5rem;
  padding: 0.5rem;
  background-color: var(--vt-c-primary);
  color: #0f66ab;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.sidebar button:hover {
  background-color: darken(var(--vt-c-primary), 10%);
}

.sidebar h4 {
  margin-top: 1rem;
  font-size: 1rem;
  color: var(--vt-c-primary);
  text-transform: uppercase;
}

.main-content {
  background-color: black; /* DICOM 查看器区域背景为黑色 */
  position: relative;
}

.info-panel h3 {
  margin: 0;
  color: var(--vt-c-primary);
}

.info-panel p {
  margin: 0.25rem 0;
}
</style>
