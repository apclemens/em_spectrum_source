<template>
    <div class="classlist">
        <div class="visible small-visible" style="left: 70.77313409838453%; width: 1.2151178139386474%"></div>
        <table>
            <tr>
                <td width="5%">
                    <span>Extremely low frequency</span>
                    <img src="./../assets/elf.jpg">
                </td>
                <td width="5%">
                    <span>Super low frequency</span>
                    <img src="./../assets/slf.svg">
                </td>
                <td width="5%">
                    <span>Ultra low frequency</span>
                    <img src="./../assets/ulf.png">
                </td>
                <td width="5%">
                    <span>Very low frequency</span>
                    <img src="./../assets/vlf.png">
                </td>
                <td width="5%">
                    <span>Low frequency</span>
                    <img src="./../assets/lf.png">
                </td>
                <td width="5%">
                    <span>Medium frequency</span>
                    <img src="./../assets/mf.png">
                </td>
                <td width="5%">
                    <span>High frequency</span>
                    <img src="./../assets/hf.png">
                </td>
                <td width="5%">
                    <span>Very high frequency</span>
                    <img src="./../assets/vhf.png">
                </td>
                <td width="5%">
                    <span>Ultra high frequency</span>
                    <img src="./../assets/uhf.png">
                </td>
                <td width="5%">
                    <span>Super high frequency</span>
                    <img src="./../assets/shf.png">
                </td>
                <td width="5%">
                    <span>Extremely high frequency</span>
                    <img src="./../assets/ehf.jpg">
                </td>
                <td width="5%">
                    <span>Far infrared</span>
                    <img src="./../assets/fi.png">
                </td>
                <td width="5%">
                    <span>Mid infrared</span>
                    <img src="./../assets/mi.jpg">
                </td>
                <td width="5%">
                    <span>Near infrared</span>
                    <img src="./../assets/ni.png">
                </td>
                <td width="5%">
                    <span>Near ultraviolet</span>
                    <img src="./../assets/nu.png">
                </td>
                <td width="5%">
                    <span>Extreme ultraviolet</span>
                    <img src="./../assets/eu.png">
                </td>
                <td width="5%">
                    <span>Soft X-rays</span>
                    <img src="./../assets/sx.png">
                </td>
                <td width="5%">
                    <span>Hard X-rays</span>
                    <img src="./../assets/hx.png">
                </td>
                <td width="5%">
                    <span>Gamma rays</span>
                    <img src="./../assets/gr.png">
                </td>
            </tr>
        </table>
    </div>
</template>

<script>
export default {
    name: 'ClassList',
}
</script>

<style>
.classlist {
    position: absolute;
    width: 100%;
    height: 100%;
}
.classlist table {
    height: 100%;
    width: 100%;
}
.classlist td {
    position: relative;
}
.classlist td img {
    position: absolute;
    width: 100%;
    bottom: 15%;;
}
.classlist td span {
    position: absolute;
    top: 0;
    font-family: 'Raleway', sans-serif;
}
</style>
