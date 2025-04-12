<template>
  <el-container style="height: 100vh;">
    <el-header style="background: #409EFF; color: white;">
      <h1>医学影像分析系统</h1>
    </el-header>
    <el-main>
      <router-view/>
    </el-main>
  </el-container>
</template>



<script setup lang="ts">
import { ElContainer, ElHeader, ElMain } from 'element-plus'
</script>
