import {createAppContainer} from 'react-navigation';
import {createStackNavigator} from 'react-navigation-stack';
import HomeScreen from './src/screens/HomeScreen';
import ListScreen from './src/screens/ListScreen';
import DeviceInfo from './src/screens/DeviceInfo';


const navigator = createStackNavigator(
  {
    Home: HomeScreen,
    List: ListScreen,
    Device: DeviceInfo,
  },
  {
    initialRouteName: 'Home',
    defaultNavigationOptions: {
      title: 'Home',
    },
  },
);

export default createAppContainer(navigator);
