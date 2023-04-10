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
      title: 'proposal',
      subtitle: 'prop desc',
    }
  },
  computed: {},
  methods: {},
  async mounted () {
    const { data } = await axios.get('/api/proposals/1')
    this.title = data.title
    this.subtitle = data.description

    new Chart(document.getElementById('myChart'), {
      type: 'bar',
      data: {
        labels: data.votes_summary.options.map(o => o.option),
        datasets: [
          {
            label: '# of Votes',
            data: data.votes_summary.options.map(o => o.count),
            borderWidth: 1,
          },
          {
            label: 'Weight',
            data: data.votes_summary.options.map(o => o.weight),
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    })
  },
}).mount('#app')
