import logo from './logo.svg';
import './App.css';
import React, { Component } from 'react';
import { HelloAPI } from './utils/api';

class Main extends Component {
  constructor (props) {
    super(props);
    this.state = {
        pod: null,
        status: null,
        version: null
    }
  }

  getData(){//请求数据函数
    HelloAPI().then(res=>{
    console.log(res)
      this.setState({
        pod:res.pod,
        status:res.status,
        version:res.version,
      })
    });
  }

  componentWillMount(){
    this.getData();
  }


  render () {
    return (
    <div>
    <div>
     pod ip - {this.state.pod}
    </div>
    <div>
     status - {this.state.status}
    </div>
    <div>
     version - {this.state.version}
     </div>
    </div>
    )
  }
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <Main/>
      </header>
    </div>
  );
}

export default App;
