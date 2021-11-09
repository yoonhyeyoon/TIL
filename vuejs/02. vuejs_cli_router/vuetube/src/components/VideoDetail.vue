<template>
  <div v-if="isShow">
    <iframe :src="videoUrl" frameborder="0"></iframe>
    <p>{{ selectItem.snippet.title | unescapeTitle }}</p>
    <p>{{ selectItem.snippet.description | unescapeTitle }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoDetail',
  props: {
    selectItem: null
  },
  filters: {
    unescapeTitle: function (title) {
      return _.unescape(title)
    }
  },
  computed: {
    videoUrl: function () {
      return `https://www.youtube.com/embed/${this.selectItem.id.videoId}`
    },
    isShow: function () {
      return !_.isEmpty(this.selectItem)
    }
  }
}
</script>

<style>

</style>