import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'
import {
  Chart,
  registerables,
} from 'https://cdn.jsdelivr.net/npm/chart.js@4.2.1/+esm'
import axios from 'https://cdn.jsdelivr.net/npm/axios@1.3.4/+esm'
import { BnCard, BnFooter, BnHero, BnNav } from './components/index.js'

// https://github.com/sgratzl/chartjs-chart-wordcloud/issues/4#issuecomment-827304369
Chart.register(...registerables)

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
    const { data } = await axios.get('/proposals/')
    this.proposals = data.map(
      p => ({
        title: p.title,
        subtitle: p.description,
        link: `/proposal/${p.proposal_id}`,
        tags: p.votes_summary.options.map(o => `${o.option}: ${o.weight}`),
      }))
  },
}).mount('#app')
