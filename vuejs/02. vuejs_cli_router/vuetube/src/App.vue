<template>
  <div id="app">
    <the-search-bar @search="onSearch"> </the-search-bar>
    <hr>
    <video-detail :select-item="selectItem"> </video-detail>
    <hr>
    <video-list :video-list="results" @selected="selectVideo"> </video-list>
  </div>
</template>

<script>
import TheSearchBar from '@/components/TheSearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'

import axios from 'axios'

export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail
  },
  data: function () {
    return {
      keyword: '',
      results: [],
      selectItem: {},
    }
  },
  methods: {
    onSearch: function (data) {
      this.keyword = data
      axios({
        method: 'get',
        url: 'https://www.googleapis.com/youtube/v3/search',
        params: {
          part: 'snippet',
          q: this.keyword,
          type: 'video',
          key: process.env.VUE_APP_YOUTUBE_API_KEY
        }
      })
      .then(res => {
        this.results = res.data.items
      })
      .catch(err => {
        console.log(err)
      })
    },
    selectVideo: function (data) {
      this.selectItem = data
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
