<template>
  <div>
    <ul v-if="videoList.length">
      <video-list-item
        v-for="(video, index) in videoList"
        :video-item="video"
        :key="index"
        @selected="selectVideo"> </video-list-item>
    </ul>


  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList',
  props: {
    videoList: Array,
  },
  components: {
    VideoListItem
  },
  methods: {
    selectVideo: function (data) {
      this.$emit('selected', data)
    }
  }
}
</script>

<style>

</style>