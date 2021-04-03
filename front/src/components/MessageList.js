import React, {Component} from 'react';


class MessageList extends Component {
    render() {
        return (
            <ul className="message-list">
                {this.props.messages.map((message, index) => {
                    return (
                        <li key={index} className={message.type === 'in' ? 'message-in' : 'message-out'}>
                            <div>{message.type === 'in' ? 'Human' : 'Bot'}</div>
                            <div>{message.text}</div>
                        </li>
                    )
                })}
            </ul>
        )
    }
}

export default MessageList;