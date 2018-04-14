import React from 'react'
import ReactDOM from 'react-dom'

import TitleBar from './components/TitleBar.jsx'

export default class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      items: []
    }
  }

  componentDidMount() {
    // call to API for user data
  }

  render() {
    return (
      <div>
        <h1>jsx code</h1>
      </div>
    )
  }
}

ReactDOM.render(<App />, document.getElementById('app'))
