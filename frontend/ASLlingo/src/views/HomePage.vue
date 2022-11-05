<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <div class="box" id="container">
        <p style="line-height: 0px;color:white;margin: 0;margin-left:2rem; margin-top:3rem; font-size:5rem;">Quiz!</p>
        <p style="line-height: 0px;color:white;margin: 0;margin-left:3rem; margin-top:4.5rem; font-size:1.5rem;">Master ASL!</p>
        <p style="line-height: 0px;color:white;margin: 0;margin-left:3rem; margin-top:2rem; font-size:1rem;">Become the winner! Win amazing prizes!</p>
        <div id="whiteSpace"></div>
        <div v-for="item in items" :key="item.id" style="">
        <ion-card @click="openModal(item.id, item.title, item.question, item.difficulty, item.color)" >
          <ion-card-header>
            <ion-card-subtitle>{{item.title}}</ion-card-subtitle>
            <ion-card-title>{{item.question}}</ion-card-title>
            
          </ion-card-header>
          <ion-card-content>
            <ion-grid>
              <ion-row>
                <ion-col>
                  <ion-text :color="item.color">
                    <p><strong>{{item.difficulty}}</strong></p>
                  </ion-text>
                  
                </ion-col>
                <ion-col></ion-col>
                <ion-col class="ion-no-padding">
                  <ion-thumbnail >
              <img alt="Silhouette of mountains" src="https://ionicframework.com/docs/img/demos/thumbnail.svg" />
            </ion-thumbnail >
                </ion-col>

              </ion-row>
            </ion-grid>
            
          </ion-card-content>
        </ion-card>
      </div>
      </div>
      <!-- create a card with a for loop -->
      

  

    </ion-content>
  </ion-page>
</template>

<script>
  import { IonContent, IonPage, IonCard, IonCardContent, IonCardTitle, IonCardSubtitle, IonThumbnail, modalController} from '@ionic/vue';
  import Modal from '../components/ModalComponent.vue';
  import { defineComponent } from 'vue';
  export default defineComponent({
    name: 'HomePage',
    components: {
      IonContent,
      IonThumbnail,
      IonPage,
      IonCard,
      IonCardContent,
      IonCardTitle,
      IonCardSubtitle

    },
    data() {
      return {
        items: [
          {id: 1, title: 'Question 1', difficulty: 'Easy', question: 'What does the fox say? Answer the question ', color: 'success'},
          {id: 2,title: 'Question 2', difficulty: 'Easy', question: 'What does the fox say? Answer the question ', color: 'success'},
          {id: 3,title: 'Question 3', difficulty: 'Hard', question: 'What does the fox say? Answer the question ', color: 'danger'},
          {id: 4,title: 'Question 4', difficulty: 'Medium', question: 'What does the fox say? Answer the question ', color: 'warning'},
          {id: 5,title: 'Question 5', difficulty: 'Easy', question: 'What does the fox say? Answer the question ', color: 'success'},
          {id: 6,title: 'Question 6', difficulty: 'Hard', question: 'What does the fox say? Answer the question ', color: 'warning'},
          {id: 7,title: 'Question 7', difficulty: 'Medium', question: 'What does the fox say? Answer the question ', color: 'warning'},
          {id: 8,title: 'Question 8', difficulty: 'Hard', question: 'What does the fox say? Answer the question ', color: 'danger'},
          {id: 9,title: 'Question 9', difficulty: 'Hard', question: 'What does the fox say? Answer the question ', color: 'danger'},
          {id: 10,title: 'Question 10', difficulty: 'Easy', question: 'What does the fox say? Answer the question ', color: 'success'}
          
        ]
      }
    },
    methods: {
      async openModal(id, title, question, difficulty, color) {
        const modal = await modalController.create({
          component: Modal,
          componentProps: {
            id : id,
            title : title,
            question :  question,
            difficulty : difficulty,
            color : color
          }
        });
      modal.present();
      // const { data, role } = await modal.onWillDismiss();
      // alert(JSON.stringify(role)) IDEA: use this to get the data back from the modal and display something then
      // console.log(data)
      
      }
    }
  })
</script>

<style scoped>
ion-content{ 
  font-family: 'Ubuntu', sans-serif;
  font-weight: 900;
  
}
#whiteSpace{
  height: 5rem;
}
.box {
  width:100vw;
  height:40rem;
  display:inline-block;
  padding-top:10px;
  background:radial-gradient(100% 35% at top,#ff7454 99%,transparent 100%);
}
ion-thumbnail {
  --size: 50px;
  --border-radius: 14px;
}
ion-card{
  margin: 25px auto;
    display: flex;
    flex-direction: column;
    width: 90% !important;
    border-radius: 10px;
    background: #f8f4f4;
  }
</style>