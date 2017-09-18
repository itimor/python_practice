<template>
  <section class="app-main" style="min-height: 100%">
    <transition name="fade" mode="out-in">
        <router-view
          transition="fade"
          transition-mode="out-in"
        >
        </router-view>
    </transition>
  </section>
</template>

<script>
  export default {
    name: 'AppMain'
  }
</script>
