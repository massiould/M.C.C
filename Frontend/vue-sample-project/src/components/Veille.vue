<template>
  <div class="welcome">
    <main class="main-content">
      <div class="articles">
        <div class="article" v-for="(article, index) in articles" :key="index">
          <img :src="article.image" alt="Article image" />
          <h2>{{ article.title }}</h2>
          <p>{{ article.summary }}</p>
        </div>
      </div>
      <aside class="news-feed">
        <h2>Fil d'actu</h2>
        <ul>
          <li v-for="(news, index) in newsFeed" :key="index">
            <time>{{ news.time }}</time>
            <p>{{ news.text }}</p>
          </li>
        </ul>
      </aside>
    </main>
  </div>
</template>

<script>
import Header from '../components/Layout/Header.vue';
import Footer from '../components/Layout/Footer.vue';
import { mapGetters } from 'vuex';

export default {
  name: 'WelcomeView',
  components: {
    Header,
    Footer
  },
  data() {
    return {
      articles: [
        {
          image: 'path/to/image1.jpg',
          title: 'Magali Delacourt-Plessix : « En matière de séparation, le droit ne peut pas tout »',
          summary: 'Interview - Profil de Magali Delacourt-Plessix...'
        },
        {
          image: 'path/to/image2.jpg',
          title: 'Tribunal de Pontoise : « Ce n\'est pas de la maîtrise de frapper sa compagne »',
          summary: 'Cour et justice - Tribunal de Pontoise...'
        }
      ],
      newsFeed: [
        { time: 'Hier: 09:00', text: 'Bilan du plan de lutte contre les fraudes sociales, fiscales et douanières' },
        { time: 'Hier: 04:30', text: 'Accord collectif fixant les modalités de négociation au sein de l\'entreprise' },
        { time: '12 Avr. 2024 - 09:01', text: 'Fichier FICOVIE : accessibilité des notaires aux informations relatives aux PER' },
        { time: '12 Avr. 2024 - 06:22', text: 'Refus d’exploitation des données saisies lors d’une perquisition : pas de recours' },
        { time: '11 Avr. 2024 - 11:58', text: 'Obligations des employeurs en matière de traçabilité des expositions aux agents chimiques cancérogènes' },
      ]
    };
  },
  computed: {
    ...mapGetters(['username'])
  }
};
</script>

<style scoped>
body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  margin: 0;
  padding: 0;
}

.welcome {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main-content {
  display: flex;
  flex: 1;
  padding: 20px;
  gap: 20px;
}

.articles {
  flex: 2;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.article {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.article img {
  width: 100%;
  height: auto;
  border-radius: 10px;
}

.article h2 {
  font-size: 18px;
  margin: 10px 0;
}

.article p {
  font-size: 14px;
  color: #555;
}

.news-feed {
  flex: 1;
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.news-feed h2 {
  font-size: 18px;
  margin-bottom: 20px;
}

.news-feed ul {
  list-style: none;
  padding: 0;
}

.news-feed ul li {
  margin-bottom: 10px;
}

.news-feed ul li time {
  font-size: 12px;
  color: #888;
}

.news-feed ul li p {
  font-size: 14px;
  color: #333;
}

.footer {
  background: #333;
  color: #fff;
  padding: 20px 0;
  text-align: center;
}
</style>
