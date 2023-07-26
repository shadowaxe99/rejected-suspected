```python
import React from 'react';
import axios from 'axios';

class SarcasmDetector extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      inputText: '',
      sarcasmOutput: '',
      feedback: ''
    };

    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleFeedbackChange = this.handleFeedbackChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleFeedbackSubmit = this.handleFeedbackSubmit.bind(this);
  }

  handleInputChange(event) {
    this.setState({inputText: event.target.value});
  }

  handleFeedbackChange(event) {
    this.setState({feedback: event.target.value});
  }

  handleSubmit(event) {
    event.preventDefault();
    axios.post('/api/detect_sarcasm', {
      text: this.state.inputText,
      api_key: 'your_api_key_here'
    })
    .then(response => {
      this.setState({sarcasmOutput: response.data});
    })
    .catch(error => {
      console.log(error);
    });
  }

  handleFeedbackSubmit(event) {
    event.preventDefault();
    axios.post('/api/feedback', {
      feedback: this.state.feedback,
      api_key: 'your_api_key_here'
    })
    .then(response => {
      console.log(response.data);
    })
    .catch(error => {
      console.log(error);
    });
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <label>
            Text to analyze:
            <input id="sarcasm-input" type="text" value={this.state.inputText} onChange={this.handleInputChange} />
          </label>
          <input type="submit" value="Detect Sarcasm" />
        </form>
        <div id="sarcasm-output">{this.state.sarcasmOutput}</div>
        <form id="feedback-form" onSubmit={this.handleFeedbackSubmit}>
          <label>
            Feedback:
            <input type="text" value={this.state.feedback} onChange={this.handleFeedbackChange} />
          </label>
          <input type="submit" value="Submit Feedback" />
        </form>
      </div>
    );
  }
}

export default SarcasmDetector;
```