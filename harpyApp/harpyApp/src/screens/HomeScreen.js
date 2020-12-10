import React from 'react';
import {Text, StyleSheet, View, TouchableOpacity, Image} from 'react-native';
import firebase from '../config';
import {createAppContainer} from 'react-navigation';
import {createStackNavigator} from 'react-navigation-stack';
import ListScreen from './ListScreen';

class HomeScreen extends React.Component {
  state = {
    buttonBGColorsArr: ['#303841', '#f3f3f3', '#f3f3f3'],
    buttonFontColorsArr: ['#f3f3f3', '#303841', '#303841'],
  };
  render() {
    return (
      <View style={styles.viewStyle}>
        <View style={{flex: 1, marginTop: 10}}>
          <Image
            style={{
              justifyContent: 'center',
              width: 400,
              height: 400,
              resizeMode: 'contain',
              alignSelf: 'center',
            }}
            source={require('../../assets/logo.png')}
          />
        </View>
        <View style={{flex: 1, marginTop: 50}}>
          <Text style={styles.text}>
            Select your scan time scale in minutes
          </Text>
          <View style={{flex: 1, flexDirection: 'row', marginTop: -150}}>
            <TouchableOpacity
              style={{
                padding: 10,
                backgroundColor: this.state.buttonBGColorsArr[0],
                marginTop: 50,
                width: 80,
                alignSelf: 'center',
                margin: 20,
                borderWidth: 1,
                borderColor: '#303841',
              }}
              onPress={() => {
                this.setState({
                  buttonBGColorsArr: ['#303841', '#f3f3f3', '#f3f3f3'],
                  buttonFontColorsArr: ['#f3f3f3', '#303841', '#303841'],
                });
                firebase
                  .database()
                  .ref('/-MHfQDfcvO17vmKEFUOc/timeScale')
                  .set(5);
              }}>
              <Text
                style={{
                  fontSize: 20,
                  color: this.state.buttonFontColorsArr[0],
                  textAlign: 'center',
                }}>
                5
              </Text>
            </TouchableOpacity>
            <TouchableOpacity
              style={{
                padding: 10,
                backgroundColor: this.state.buttonBGColorsArr[1],
                marginTop: 50,
                width: 80,
                alignSelf: 'center',
                margin: 20,
                borderWidth: 1,
                borderColor: '#303841',
              }}
              onPress={() => {
                this.setState({
                  buttonBGColorsArr: ['#f3f3f3', '#303841', '#f3f3f3'],
                  buttonFontColorsArr: ['#303841', '#f3f3f3', '#303841'],
                });
                firebase
                  .database()
                  .ref('/-MHfQDfcvO17vmKEFUOc/timeScale')
                  .set(15);
              }}>
              <Text
                style={{
                  fontSize: 20,
                  color: this.state.buttonFontColorsArr[1],
                  textAlign: 'center',
                }}>
                15
              </Text>
            </TouchableOpacity>
            <TouchableOpacity
              style={{
                padding: 10,
                backgroundColor: this.state.buttonBGColorsArr[2],
                marginTop: 50,
                width: 80,
                alignSelf: 'center',
                margin: 20,
                borderWidth: 1,
                borderColor: '#303841',
              }}
              onPress={() => {
                this.setState({
                  buttonBGColorsArr: ['#f3f3f3', '#f3f3f3', '#303841'],
                  buttonFontColorsArr: ['#303841', '#303841', '#f3f3f3'],
                });
                firebase
                  .database()
                  .ref('/-MHfQDfcvO17vmKEFUOc/timeScale')
                  .set(30);
              }}>
              <Text
                style={{
                  fontSize: 20,
                  color: this.state.buttonFontColorsArr[2],
                  textAlign: 'center',
                }}>
                30
              </Text>
            </TouchableOpacity>
          </View>
        </View>
        <View style={{flex: 1, marginTop: -100}}>
          <Text style={styles.text}>
            Press scan to show the devices around you
          </Text>
          <TouchableOpacity
            style={styles.buttonStyle}
            onPress={() => this.props.navigation.navigate('List')}>
            <Text style={styles.textStyle}>Scan</Text>
          </TouchableOpacity>
        </View>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  text: {
    fontSize: 20,
    textAlign: 'center',
    fontFamily: 'Menlo',
  },
  viewStyle: {
    flex: 1,
    alignItems: 'center',
  },
  textStyle: {
    fontSize: 20,
    color: '#ffffff',
    textAlign: 'center',
    fontFamily: 'Menlo',
  },
  buttonStyle: {
    padding: 10,
    backgroundColor: '#303841',
    width: 200,
    alignSelf: 'center',
    marginTop: 35,
  },
});

export default HomeScreen;
