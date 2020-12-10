import * as firebase from 'firebase';

let config = {
  apiKey: 'AIzaSyBJqqj1jgw0sNgCD-iC_uKbKPLqdg5Ytp8',
  authDomain: 'harpy-c8519.firebaseapp.com',
  databaseURL: 'https://harpy-c8519.firebaseio.com/',
  projectId: 'harpy-c8519',
  storageBucket: 'harpy-c8519.appspot.com',
};
firebase.initializeApp(config);

export default firebase;
