<template>
  <div>
    <h1>My first youtube project</h1>
    <input type="text" v-model.trim="searchKeyword" @keyup.enter="onSearch">
    <button @click="onSearch">검색</button>
  </div>
</template>

<script>
export default {
 name: 'TheSearchBar',
 data: function () {
   return {
     searchKeyword: ''
   }
 },
 methods: {
   onSearch: function () {
     if (this.searchKeyword.length !== 0) {
     this.$emit('search', this.searchKeyword)
     }
   }
 }
}
</script>

<style>

</style>