<template>
    <ion-page>
        <ion-header>
        <ion-toolbar>
            <ion-buttons slot="start">
            <ion-button color="medium" @click="cancel">
                <ion-icon :md="icon.mdBack" :ios="icon.iosBack" ></ion-icon>
            </ion-button>
            </ion-buttons>
            <ion-grid>
                <ion-row style="margin-bottom:0;padding-bottom:0">
                    <ion-title style="margin-bottom:0;padding-bottom:0">{{title}}</ion-title>
                </ion-row>
                <ion-row>
                    <ion-label style="padding-left:1.2rem">
                        <ion-text :color="color">
                            <p><strong>{{difficulty}}</strong></p>
                        </ion-text>
                    </ion-label>
                </ion-row>
            </ion-grid>
        </ion-toolbar>
        </ion-header>
        <ion-content :fullscreen="true" v-if="difficulty=='Easy'">
            <div class="box">
                <div id="whiteSpace"></div>
                <ion-grid>
                    <ion-row style="margin-bottom:0;padding-bottom:0">
                        <p style="margin-bottom:5px;padding-bottom:10px" id="questionHeader">{{question}}</p>
                    </ion-row>
                    <ion-row style="margin-top:0;padding-top:0">
                        <ion-col style="margin-top:0;padding-top:0">
                            <p style="margin-top:0;padding-top:0" id="questionHint">Hint: Click the Camera icon to select your choice.</p>
                        </ion-col>
                    </ion-row>
                    <ion-row>
                        <ion-col v-for="item in optionset1" :key="item.id" style="">
                            <ion-card>
                                <img alt="Silhouette of mountains" height="160" width="160" :src=item.link />
                                <ion-card-header>
                                    <ion-card-title>{{item.title}}</ion-card-title>
                                </ion-card-header>
                            </ion-card>
                        </ion-col>
                    </ion-row>
                    <ion-row>
                        <ion-col v-for="item in optionset2" :key="item.id" style="">
                            <ion-card>
                                <img alt="Silhouette of mountains" height="160" width="160" :src=item.link />
                                <ion-card-header>
                                    <ion-card-title>{{item.title}}</ion-card-title>
                                </ion-card-header>
                            </ion-card>
                        </ion-col>
                    </ion-row>
                </ion-grid>        
                <div style="text-align:center">
                    <ion-button @click="takeVideo" shape="circle" id="send">
                        <ion-icon :md="icon.md" :ios="icon.ios"></ion-icon>
                    </ion-button>
                </div>
            </div>
            <button id="modalButton" style="display:none"></button>
            <ion-modal trigger="modalButton" ref="modal" :initial-breakpoint="0.25" :breakpoints="[0, 0.25, 0.5, 0.75]">
              <ion-header>
            <ion-toolbar class="ion-padding-horizontal" >
              <ion-text>
                <p id="resultsModal">Results:</p>
              </ion-text>
            </ion-toolbar>
          </ion-header>
                <ion-content class="ion-padding">
                  <ion-list :inset="true">
                  <ion-item>
                    <ion-label>
                      <ion-text :color="ansColor"><h2>{{ansText}}</h2></ion-text>
                    </ion-label>
                  </ion-item>

                  <ion-item>
                    <ion-label>
                      <ion-text color="success"><h2>Correct Answer</h2></ion-text>
                      <p>{{answer.title}}</p>
                      <img :src=answer.link height="50px" width="50px" alt="Tasd">
                    </ion-label>
                  </ion-item>

                </ion-list>
                </ion-content>
            </ion-modal>
        </ion-content>
        <ion-content :fullscreen="true" v-else>
            <div class="box">
                <div id="whiteSpace"></div>
                <ion-grid>
                    <ion-row style="margin-bottom:0;padding-bottom:0">
                        <p style="margin-bottom:5px;padding-bottom:10px" id="questionHeader">{{question}}</p>
                    </ion-row>
                    <ion-row style="margin-top:0;padding-top:0">
                        <ion-col style="margin-top:0;padding-top:0">
                            <p style="margin-top:0;padding-top:0" id="questionHint">Hint: Click the Camera icon to select your choice.</p>
                        </ion-col>
                    </ion-row>
                </ion-grid>        
                <div style="text-align:center">
                    <ion-img :src="link" alt="Tasd" style="margin-bottom:20px"></ion-img>
                    <ion-button @click="takeVideo" shape="circle" id="send">
                        <ion-icon :md="icon.md" :ios="icon.ios"></ion-icon>
                    </ion-button>
                </div>
            </div>
            <button id="modalButton" style="display:none"></button>
            <ion-modal trigger="modalButton" ref="modal" :initial-breakpoint="0.25" :breakpoints="[0, 0.25, 0.5, 0.75]">
              <ion-header>
            <ion-toolbar class="ion-padding-horizontal" >
              <ion-text>
                <p id="resultsModal">Results:</p>
              </ion-text>
            </ion-toolbar>
          </ion-header>
                <ion-content class="ion-padding">
                <ion-list :inset="true">
                  <ion-item>
                    <ion-label>
                      <ion-text :color="ansColor"><h2 style="font-size:1.5rem">{{ansText}}</h2></ion-text>
                    </ion-label>
                  </ion-item>

                  <ion-item>
                    <ion-label>
                      <ion-text color="success"><h2>Correct Answer</h2></ion-text>
                      <p>{{answer.title}}</p>
                      <img :src="answer.link" >
                    </ion-label>
                  </ion-item>

                </ion-list>
                </ion-content>
            </ion-modal>
            
        </ion-content>
    </ion-page>
  </template>
  
  <script >
    import {
      IonContent,
      IonIcon,
      IonModal,
      IonHeader,
      IonTitle,
      IonText,
      IonCard,
      IonCardHeader,
        IonCardTitle,
        IonList,
        IonItem,
        IonLabel,
      IonToolbar,
      IonPage,
      IonButtons,
      IonButton,
      IonGrid, IonRow, IonCol, IonImg,
      modalController,
      loadingController 
    } from '@ionic/vue';
    import { defineComponent } from 'vue';
    import { cameraOutline, arrowBackOutline  } from 'ionicons/icons';
    import {MediaCapture} from '@awesome-cordova-plugins/media-capture';
  import {Capacitor} from '@capacitor/core';
  import axios from 'axios';
    export default defineComponent({
      name: 'ModalVue',
      components: { 
        IonContent,
        IonCard, 
        IonLabel, 
        IonPage,
        IonCardHeader,
        IonList,
        IonItem,
        IonCardTitle,
        IonHeader, 
        IonModal, 
        IonTitle, 
        IonToolbar, IonButtons, IonButton,IonIcon, IonGrid, IonRow, IonCol, IonImg,IonText },

      data() {
        return {
          ansColor: 'danger',
          ansText: 'Incorrect Answer!',
          answerList: [
            {
              id: 1,
              heading: "Your Answer",
              link: "https://ionicframework.com/docs/img/demos/thumbnail.svg",
              color: "success",
              answer: "answer"
            },
            {
              id: 2,
              heading: "Correct Answer",
              link: "https://ionicframework.com/docs/img/demos/thumbnail.svg",
              color: "success",
              answer: "answer"
            }
          ],
            videoInfo: {},
            icon: {
                md: cameraOutline,
                ios: cameraOutline,
                mdBack: arrowBackOutline,
                iosBack: arrowBackOutline
            }
        }
      },
      props: {
        answer: {
          type: Object,
        },
        id: {
          type: Number,
          default: null,
        },
        title: {
          type: String,
          default: null,
        },
        question: {
          type: String,
          default: null,
        },
        difficulty: {
          type: String,
          default: null,
        },
        color: {
          type: String,
          default: null,
        },
        optionset1: {
          type: Array,
          default: null,
        },
        optionset2: {
          type: Array,
          default: null,
        },
        link: {
          type: String,
          default: null,
        },
      },
      // mounted(){document.getElementById("modalButton").click();},
      methods: {
        cancel() {
          return modalController.dismiss('cancel', this.videoInfo);
        },

        takeVideo: async function () {
          const that = this // DEBUG
        try {
            
          const options = {
            duration: 4,
            limit: 1,
            quality: 1
          };
          const result = await MediaCapture.captureVideo(options);
          this.videoInfo = result[0];
          // console.log("videoInfo", JSON.stringify(result[0]));
          const blob = await fetch(
            Capacitor.convertFileSrc(this.videoInfo.fullPath)
          ).then(r => r.blob());
          const formData = new FormData();
          formData.append("file", blob, this.videoInfo.name);
          // convert video blob to base64
          let reader = new FileReader();
          reader.readAsDataURL(blob);
          reader.onloadend = async function() {
            let base64data = reader.result;
            let trimmed = base64data.substring(base64data.indexOf(",") + 1);
           console.log(trimmed); // DEBUG
           const loading = await loadingController.create({
            message: 'Please wait...'
            });  
            await loading.present();
            
          axios({
            method: "post",
            url: "https://df85-2620-101-c040-85c-872-da75-28a3-1291.ngrok.io/upload/",
            data: JSON.stringify({
              _data: trimmed
            }),
          headers: {
            "Content-Type": "application/json"
          }
          }).then((response) => {
                loading.dismiss();
                if (response.status == 200){
                  // alert (JSON.stringify(response.data));
                  document.getElementById("modalButton").click();
                  // search in json stringy for answer title
                  if (JSON.stringify(response.data).includes(that.answer.title)) {
                    that.ansColor = 'success';
                    that.ansText = 'Correct Answer!';
                  }
                }
          });
          };
        } catch (error) {
            // NEVER PUT ALERT HERE
          console.log(error);
      }
    }
      },
    });
  </script>

  <style scoped>
ion-button#send::part(native) {
  width: 50px;
  height: 50px;
  border-radius: 100% !important;
}
p#questionHeader{ 
  font-family: 'Ubuntu', sans-serif;
  font-weight: 900;
    font-size: 1.5rem;
    text-align: center;
    color: white; 
}
p#questionHint{ 
  font-family: 'Ubuntu', sans-serif;
  font-weight: 400;
    font-size: 1rem;
    text-align: center;
    color: white; 
}
p#resultsModal{ 
  font-family: 'Ubuntu', sans-serif;
  font-weight: 900;
    font-size: 1.2rem;
    text-align: left;
}
.box {
  width:100vw;
  height:40rem;
  display:inline-block;
  padding-top:10px;
  background:radial-gradient(100% 35% at top,#ff7454 99%,transparent 100%);

}
ion-img {
    height:100%;
    width: 20rem !important;
    margin: auto;
    align-items: center;
}

</style>