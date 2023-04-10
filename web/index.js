import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'
import axios from 'https://cdn.jsdelivr.net/npm/axios@1.3.4/+esm'
import { BnCard, BnFooter, BnHero, BnNav } from './components/index.js'


createApp({
  components: {
    BnCard, BnNav, BnFooter, BnHero,
  },
  data () {
    return {
      proposals: [],
    }
  },
  computed: {},
  methods: {},
  async mounted () {
    const { data } = await axios.get('/api/proposals')
    this.proposals = data.map(
      p => ({
        title: p.title,
        subtitle: p.description,
        link: `/proposal/${p.id}`,
        tags: p.votes_summary.options.map(o => `${o.option}: ${o.weight}`),
      }))
  },
}).mount('#app')
