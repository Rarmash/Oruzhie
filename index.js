const { Client, MessageEmbed } = require('discord.js');
const client = new Client({ partials: ['MESSAGE'] });

client.login('OTM1NTYwOTY4Nzc4NDQ4OTQ3.YfAbDA.NdLXCXZAwOMWrqKrAsHnVlImjsg');

client.on('ready', () => {
    console.log(`${client.user.tag} logged in.`);
    client.user.setActivity('за ореолом Дзета', { type: 'WATCHING' })
		  .then(presence => console.log(`Activity set to ${presence.activities[0].name}`))
		  .catch(console.error);
});

client.on('messageDelete', message => {
    if(!message.partial) {
        const channel = client.channels.cache.get('952519133117960192');
        if((channel) && (channel !== '647756597904408617')) {
            const embed = new MessageEmbed()
                .setTitle('Удалённое сообщение')
                .setColor('#209af8')
                .addField('Автор', `<@${message.author.id}>`, true)
                .addField('Канал', `<#${message.channel.id}>`, true)
                .setDescription(message.content)
                .setTimestamp();
            channel.send(embed);
        }
    }
}); 