import React from 'react'
import ReactDOM from 'react-dom'
import $ from 'jquery'

import TitleBar from './components/TitleBar.jsx'
import HeadBanner from './components/Header.jsx'
import DriverTable from './components/DriverTable.jsx'
import IncidentTable from './components/IncidentTable.jsx'

export default class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      incidents: [],
      users: [],
      screen: 'incident'
    }
    this.poll = this.poll.bind(this)
  }

  poll() {
    this.setState({ ticker: this.state.ticker + 1 })
    $.ajax({
      url: `/incidents`,
      type: 'GET',
      contentType: 'application/json',
      success: data => {
        this.setState({ incidents: data })
      },
      error: err => {
        console.error(err)
      }
    })
    $.ajax({
      url: `/users`,
      type: 'GET',
      contentType: 'application/json',
      success: data => {
        this.setState({ users: data })
      },
      error: err => {
        console.error(err)
      }
    })
  }

  submit(a, b) {
    $.ajax({
      url: `/resolve_incident`,
      type: 'POST',
      contentType: 'application/json',
      dataType: 'json',
      data: JSON.stringify({
        incident_id: a,
        issue: b
      }),
      success: data => {
        this.render()
      },
      error: err => {
        console.error(err)
      }
    })
  }

  componentDidMount() {
    this.interval = setInterval(this.poll, 1000)
    // this.poll()
  }

  componentWillUnmountMount() {
    clearInterval(this.interval)
  }

  changeScreen(screen) {
    this.setState({ screen: screen })
  }

  render() {
    return (
      <div>
        <HeadBanner
          incident={this.state.incidents.length}
          user={this.state.users.length}
          changeScreen={this.changeScreen.bind(this)}
        />
        {this.state.screen === 'incident' ? (
          <IncidentTable
            data={this.state.incidents}
            submit={this.submit.bind(this)}
          />
        ) : (
          <DriverTable data={this.state.users} />
        )}
      </div>
    )
  }
}

ReactDOM.render(<App />, document.getElementById('app'))
