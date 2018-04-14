import React from 'react'
import ReactDOM from 'react-dom'

import TitleBar from './components/TitleBar.jsx'
import HeadBanner from './components/Header.jsx'
import DriverTable from './components/DriverTable.jsx'

export default class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      ticker: 1,
      columns: ['test1', 'test2', 'test3'],
      users: [{ test1: 'field1' }]
    }
    this.poll = this.poll.bind(this)
  }

  poll() {
    this.setState({ ticker: this.state.ticker + 1 })
    // call API
  }

  componentDidMount() {
    // this.interval = setInterval(this.poll, 1000)
  }

  componentWillUnmountMount() {
    clearInterval(this.interval)
  }

  render() {
    return (
      <div>
        <HeadBanner />
        <DriverTable ticker={this.state.ticker} />>
      </div>
    )
  }
}

ReactDOM.render(<App />, document.getElementById('app'))
