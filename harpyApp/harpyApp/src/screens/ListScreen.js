import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  FlatList,
  TouchableOpacity,
  SafeAreaView,
} from 'react-native';
import firebase from '../config';
import Icon from 'react-native-vector-icons/MaterialIcons';
var data = [{1: 1}];
console.disableYellowBox = true;

class ListScreen extends React.Component {
  state = {
    listData: [],
  };
  componentDidMount() {
    firebase
      .database()
      .ref('/-MHfQDfcvO17vmKEFUOc')
      .on('value', (querySnapShot) => {
        data = [querySnapShot.val()];
        this.setState({listData: data});
      });
  }

  render() {
    //console.log('this is data', data);
    return (
      <SafeAreaView>
        <View>
          <Text
            style={{
              fontFamily: 'Menlo',
              alignSelf: 'center',
              color: 'black',
              fontSize: 20,
            }}>
            {Object.keys(data[0]).length - 1} Devices Were Detected
          </Text>
          <FlatList
            data={this.state.listData}
            renderItem={({item}) => {
              return (
                <SafeAreaView style={styles.container}>
                  {Object.keys(item).map((value, index) => {
                    return (
                      value !== 'timeScale' &&
                      value !== 'scan' && (
                        <TouchableOpacity
                          onPress={() =>
                            this.props.navigation.navigate('Device', {
                              device: item[value],
                            })
                          }
                          style={styles.buttonStyle}>
                          <Icon
                            name={item[value].iconName}
                            size={30}
                            color={item[value].safety ? 'green' : 'red'}
                            style={styles.iconStyle}
                          />
                          <View style={styles.iconSeparator} />
                          <View>
                            <Text style={styles.textStyle}>
                              Device Type: {item[value]['Device Type']}
                            </Text>
                            <Text style={styles.textStyle}>MAC: {value}</Text>
                          </View>

                          <Icon
                            name={'arrow-right'}
                            size={30}
                            color="#f3f3f3"
                            style={{
                              alignSelf: 'center',
                            }}
                          />
                        </TouchableOpacity>
                      )
                    );
                  })}
                </SafeAreaView>
              );
            }}
          />
        </View>
      </SafeAreaView>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f3f3f3',
  },
  textStyle: {
    fontSize: 20,
    color: '#f3f3f3',
    padding: 1,
    marginLeft: 10,
    fontFamily: 'Menlo',
  },
  buttonStyle: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    padding: 5,
    backgroundColor: '#303841',
    marginTop: 1,
    width: '100%',
    flex: 1,
  },
  iconSeparator: {
    backgroundColor: '#f3f3f3',
    width: 1,
    height: 40,
  },
  iconStyle: {
    padding: 5,
  },
});

export default ListScreen;
