import React from 'react';
import {View, Text, StyleSheet, TouchableOpacity} from 'react-native';
import {SafeAreaView} from 'react-navigation';
import firebase from '../config';
var data;

class DeviceInfo extends React.Component {
  state = {
    known: this.props.navigation.getParam('device')['safety'],
  };

  componentDidMount() {
    const item = this.props.navigation.getParam('device');
    firebase
      .database()
      .ref(`/-MHfQDfcvO17vmKEFUOc/${item['Device MAC']}/safety`)
      .on('value', (querySnapShot) => {
        data = [querySnapShot.val()];
        this.setState({known: data});
        console.log('this is known', this.state.known);
      });
  }

  render() {
    const item = this.props.navigation.getParam('device');
    var headerbgColor = item['safety'] ? 'green' : 'red';
    var unknownbgColor = item['safety'] ? 'white' : 'red';
    var knownbgColor = item['safety'] ? 'green' : 'white';

    console.log('item inside device info', item);

    return (
      <SafeAreaView>
        <View style={styles.viewStyle}>
          <Text
            style={{
              fontSize: 25,
              color: 'white',
              backgroundColor: headerbgColor,
              textAlign: 'center',
              padding: 10,
              borderRadius: 5,
              fontFamily: 'Menlo',
              marginBottom: 5,
            }}>
            Device Information
          </Text>
          <Text style={styles.textStyle}>Type: {item['Device Type']}</Text>
          <Text style={styles.textStyle}>Name: {item['Device Name']}</Text>
          <Text style={styles.textStyle}>
            MAC Address: {item['Device MAC']}
          </Text>
          <Text style={styles.textStyle}>
            Active Time: {item['Device Total Active Time']} (Seconds)
          </Text>
          <Text style={styles.textStyle}>
            Protocols Used: {item['Number of Protocols Used']}
          </Text>
          <Text style={styles.textStyle}>
            Servers: {item['Number of Servers']}
          </Text>
          <Text style={styles.textStyle}>
            Average Packet Size:{' '}
            {Number(item['Device Avarage Packet Size'].toFixed(1))} (Bytes)
          </Text>
          <Text style={styles.textStyle}>
            Data Flow Rate: {Number(item['Device Flow Rate'].toFixed(1))}{' '}
            (Bytes/Second)
          </Text>
          <Text style={styles.textStyle}>
            Data Flow Volume: {item['Device Total Flow Volume']} (Bytes)
          </Text>
          <View
            style={{
              flex: 1,
              flexDirection: 'row',
              justifyContent: 'space-evenly',
              marginTop: 100,
            }}>
            <TouchableOpacity
              style={{
                backgroundColor: unknownbgColor,
                marginTop: 50,
                width: 190,
                height: 50,
                alignSelf: 'center',
                margin: 20,
                borderWidth: 1,
                borderColor: '#303841',
                justifyContent: 'center',
                alignItems: 'center',
              }}
              onPress={() => {
                firebase
                  .database()
                  .ref(`/-MHfQDfcvO17vmKEFUOc/${item['Device MAC']}/safety`)
                  .set(!item['safety']);
                this.setState({known: !this.state.known});
                this.forceUpdate();
              }}>
              <Text
                style={{
                  fontSize: 20,
                  fontFamily: 'Menlo',
                }}>
                Unknown Device
              </Text>
            </TouchableOpacity>
            <TouchableOpacity
              style={{
                backgroundColor: knownbgColor,
                marginTop: 50,
                width: 190,
                height: 50,
                alignSelf: 'center',
                margin: 20,
                borderWidth: 1,
                borderColor: '#303841',
                justifyContent: 'center',
                alignItems: 'center',
              }}
              onPress={() => {
                firebase
                  .database()
                  .ref(`/-MHfQDfcvO17vmKEFUOc/${item['Device MAC']}/safety`)
                  .set(!item['safety']);
                this.setState({known: !this.state.known});
                this.forceUpdate();
              }}>
              <Text
                style={{
                  fontSize: 20,
                  fontFamily: 'Menlo',
                }}>
                Known Device
              </Text>
            </TouchableOpacity>
          </View>
        </View>
      </SafeAreaView>
    );
  }
}

const styles = StyleSheet.create({
  viewStyle: {},
  textStyle: {
    fontSize: 20,
    color: 'black',
    padding: 10,
    borderRadius: 5,
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

export default DeviceInfo;
